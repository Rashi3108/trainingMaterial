#!/usr/bin/env python3
"""
deploy.py - Sample solution for main deployment script

This script demonstrates all Python concepts from the presentation:
- Variables and data types
- Input/output operations
- Conditional statements
- Loops
- Functions and code reusability
- Error handling
- File operations
- Command-line argument parsing
"""

import os
import sys
import json
import yaml
import logging
import argparse
import subprocess
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class DeploymentError(Exception):
    """Custom exception for deployment errors"""
    pass

class DeploymentManager:
    """Main deployment management class"""
    
    def __init__(self, config_path: str, dry_run: bool = False):
        """Initialize deployment manager"""
        self.config_path = Path(config_path)
        self.dry_run = dry_run
        self.start_time = datetime.now()
        self.deployment_id = f"deploy-{self.start_time.strftime('%Y%m%d-%H%M%S')}"
        
        # Initialize configuration storage
        self.app_config: Dict = {}
        self.deployment_config: Dict = {}
        self.monitoring_config: Dict = {}
        
        # Deployment tracking
        self.deployment_steps: List[str] = []
        self.failed_steps: List[str] = []
        self.deployment_status = "initialized"
        
        # Setup logging
        self.setup_logging()
        self.logger.info(f"Deployment manager initialized - ID: {self.deployment_id}")
    
    def setup_logging(self):
        """Configure logging for the deployment script"""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        log_file = log_dir / f"deployment-{self.deployment_id}.log"
        
        # Configure logging format
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        
        # Setup file and console handlers
        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info("Logging system initialized")
    
    def load_configuration(self) -> bool:
        """Load and validate YAML configuration files"""
        try:
            config_files = {
                'app_config': self.config_path / 'app-config.yml',
                'deployment_config': self.config_path / 'deployment-config.yml',
                'monitoring_config': self.config_path / 'monitoring-config.yml'
            }
            
            # Load each configuration file
            for config_name, config_file in config_files.items():
                if not config_file.exists():
                    raise DeploymentError(f"Configuration file not found: {config_file}")
                
                try:
                    with open(config_file, 'r') as f:
                        config_data = yaml.safe_load(f)
                    
                    # Store configuration
                    setattr(self, config_name, config_data)
                    self.logger.info(f"Loaded configuration: {config_name}")
                    
                except yaml.YAMLError as e:
                    raise DeploymentError(f"Invalid YAML in {config_file}: {e}")
            
            # Validate configuration structure
            self._validate_configuration_structure()
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to load configuration: {e}")
            return False
    
    def _validate_configuration_structure(self):
        """Validate that required configuration fields are present"""
        required_app_fields = ['application', 'database', 'api']
        required_deployment_fields = ['deployment', 'container', 'networking']
        
        # Validate app configuration
        for field in required_app_fields:
            if field not in self.app_config:
                raise DeploymentError(f"Missing required field in app config: {field}")
        
        # Validate deployment configuration
        for field in required_deployment_fields:
            if field not in self.deployment_config:
                raise DeploymentError(f"Missing required field in deployment config: {field}")
        
        self.logger.info("Configuration structure validation passed")
    
    def validate_prerequisites(self) -> bool:
        """Check system prerequisites before deployment"""
        try:
            self.logger.info("Checking system prerequisites...")
            
            # Check disk space (minimum 1GB free)
            disk_usage = self._check_disk_space()
            if disk_usage > 90:
                self.logger.warning(f"Disk usage is high: {disk_usage}%")
                if disk_usage > 95:
                    raise DeploymentError("Insufficient disk space for deployment")
            
            # Check memory availability
            memory_usage = self._check_memory_usage()
            if memory_usage > 90:
                self.logger.warning(f"Memory usage is high: {memory_usage}%")
            
            # Verify network connectivity
            if not self._check_network_connectivity():
                raise DeploymentError("Network connectivity check failed")
            
            # Check required tools
            required_tools = ['docker', 'curl', 'python3']
            for tool in required_tools:
                if not self._check_tool_availability(tool):
                    raise DeploymentError(f"Required tool not available: {tool}")
            
            # Check permissions
            if not self._check_permissions():
                raise DeploymentError("Insufficient permissions for deployment")
            
            self.logger.info("Prerequisites validation passed")
            return True
            
        except Exception as e:
            self.logger.error(f"Prerequisites validation failed: {e}")
            return False
    
    def _check_disk_space(self) -> float:
        """Check available disk space"""
        try:
            result = subprocess.run(['df', '-h', '.'], capture_output=True, text=True)
            lines = result.stdout.strip().split('\n')
            if len(lines) >= 2:
                usage_line = lines[1].split()
                usage_percent = float(usage_line[4].rstrip('%'))
                return usage_percent
        except Exception:
            self.logger.warning("Could not check disk space")
        return 0.0
    
    def _check_memory_usage(self) -> float:
        """Check memory usage"""
        try:
            with open('/proc/meminfo', 'r') as f:
                meminfo = f.read()
            
            # Parse memory information
            mem_total = 0
            mem_available = 0
            
            for line in meminfo.split('\n'):
                if line.startswith('MemTotal:'):
                    mem_total = int(line.split()[1])
                elif line.startswith('MemAvailable:'):
                    mem_available = int(line.split()[1])
            
            if mem_total > 0:
                usage_percent = ((mem_total - mem_available) / mem_total) * 100
                return usage_percent
                
        except Exception:
            self.logger.warning("Could not check memory usage")
        return 0.0
    
    def _check_network_connectivity(self) -> bool:
        """Check network connectivity"""
        try:
            # Test connectivity to a reliable endpoint
            result = subprocess.run(
                ['curl', '-s', '--connect-timeout', '5', 'https://httpbin.org/status/200'],
                capture_output=True
            )
            return result.returncode == 0
        except Exception:
            return False
    
    def _check_tool_availability(self, tool: str) -> bool:
        """Check if a required tool is available"""
        try:
            result = subprocess.run(['which', tool], capture_output=True)
            return result.returncode == 0
        except Exception:
            return False
    
    def _check_permissions(self) -> bool:
        """Check if we have necessary permissions"""
        try:
            # Check write permissions in current directory
            test_file = Path('permission_test.tmp')
            test_file.write_text('test')
            test_file.unlink()
            return True
        except Exception:
            return False
    
    def pre_deployment_checks(self) -> bool:
        """Perform pre-deployment validation"""
        try:
            self.logger.info("Performing pre-deployment checks...")
            
            # Validate application configuration
            app_name = self.app_config.get('application', {}).get('name')
            if not app_name:
                raise DeploymentError("Application name not specified in configuration")
            
            # Check deployment strategy
            strategy = self.deployment_config.get('deployment', {}).get('strategy', 'rolling')
            valid_strategies = ['rolling', 'blue-green', 'canary']
            if strategy not in valid_strategies:
                raise DeploymentError(f"Invalid deployment strategy: {strategy}")
            
            # Validate container configuration
            container_config = self.deployment_config.get('container', {})
            if not container_config.get('image'):
                raise DeploymentError("Container image not specified")
            
            # Test database connectivity (if configured)
            if 'database' in self.app_config:
                if not self._test_database_connectivity():
                    self.logger.warning("Database connectivity test failed")
            
            # Validate API endpoints
            if not self._validate_api_endpoints():
                self.logger.warning("API endpoint validation failed")
            
            self.logger.info("Pre-deployment checks completed successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Pre-deployment checks failed: {e}")
            return False
    
    def _test_database_connectivity(self) -> bool:
        """Test database connectivity"""
        try:
            db_config = self.app_config.get('database', {}).get('primary', {})
            host = db_config.get('host', 'localhost')
            port = db_config.get('port', 5432)
            
            # Simple connectivity test using netcat or telnet
            result = subprocess.run(
                ['nc', '-z', '-w', '5', host, str(port)],
                capture_output=True
            )
            return result.returncode == 0
        except Exception:
            return False
    
    def _validate_api_endpoints(self) -> bool:
        """Validate API endpoints configuration"""
        try:
            api_config = self.app_config.get('api', {})
            base_url = api_config.get('base_url')
            
            if not base_url:
                return False
            
            # Test health endpoint if available
            health_endpoint = api_config.get('endpoints', {}).get('health')
            if health_endpoint:
                full_url = f"{base_url}{health_endpoint}"
                result = subprocess.run(
                    ['curl', '-s', '-f', '--connect-timeout', '10', full_url],
                    capture_output=True
                )
                return result.returncode == 0
            
            return True
        except Exception:
            return False
    
    def execute_deployment(self) -> bool:
        """Execute the main deployment process"""
        try:
            self.logger.info("Starting deployment execution...")
            self.deployment_status = "in_progress"
            
            # Get deployment strategy
            strategy = self.deployment_config.get('deployment', {}).get('strategy', 'rolling')
            
            # Execute deployment based on strategy
            if strategy == 'rolling':
                success = self._execute_rolling_deployment()
            elif strategy == 'blue-green':
                success = self._execute_blue_green_deployment()
            elif strategy == 'canary':
                success = self._execute_canary_deployment()
            else:
                raise DeploymentError(f"Unsupported deployment strategy: {strategy}")
            
            if success:
                self.deployment_status = "completed"
                self.logger.info("Deployment execution completed successfully")
            else:
                self.deployment_status = "failed"
                self.logger.error("Deployment execution failed")
            
            return success
            
        except Exception as e:
            self.deployment_status = "failed"
            self.logger.error(f"Deployment execution failed: {e}")
            return False
    
    def _execute_rolling_deployment(self) -> bool:
        """Execute rolling deployment strategy"""
        try:
            self.logger.info("Executing rolling deployment...")
            
            # Deployment steps for rolling strategy
            steps = [
                "pull_container_image",
                "update_configuration",
                "deploy_new_version",
                "health_check_new_version",
                "update_load_balancer",
                "cleanup_old_version"
            ]
            
            for step in steps:
                self.logger.info(f"Executing step: {step}")
                
                if self.dry_run:
                    self.logger.info(f"DRY RUN: Would execute {step}")
                    time.sleep(1)  # Simulate execution time
                else:
                    success = self._execute_deployment_step(step)
                    if not success:
                        self.failed_steps.append(step)
                        raise DeploymentError(f"Deployment step failed: {step}")
                
                self.deployment_steps.append(step)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Rolling deployment failed: {e}")
            return False
    
    def _execute_blue_green_deployment(self) -> bool:
        """Execute blue-green deployment strategy"""
        try:
            self.logger.info("Executing blue-green deployment...")
            
            steps = [
                "prepare_green_environment",
                "deploy_to_green",
                "test_green_environment",
                "switch_traffic_to_green",
                "verify_green_deployment",
                "cleanup_blue_environment"
            ]
            
            for step in steps:
                self.logger.info(f"Executing step: {step}")
                
                if self.dry_run:
                    self.logger.info(f"DRY RUN: Would execute {step}")
                    time.sleep(1)
                else:
                    success = self._execute_deployment_step(step)
                    if not success:
                        self.failed_steps.append(step)
                        raise DeploymentError(f"Deployment step failed: {step}")
                
                self.deployment_steps.append(step)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Blue-green deployment failed: {e}")
            return False
    
    def _execute_canary_deployment(self) -> bool:
        """Execute canary deployment strategy"""
        try:
            self.logger.info("Executing canary deployment...")
            
            steps = [
                "deploy_canary_version",
                "route_small_traffic_to_canary",
                "monitor_canary_metrics",
                "gradually_increase_canary_traffic",
                "validate_canary_performance",
                "complete_canary_rollout"
            ]
            
            for step in steps:
                self.logger.info(f"Executing step: {step}")
                
                if self.dry_run:
                    self.logger.info(f"DRY RUN: Would execute {step}")
                    time.sleep(1)
                else:
                    success = self._execute_deployment_step(step)
                    if not success:
                        self.failed_steps.append(step)
                        raise DeploymentError(f"Deployment step failed: {step}")
                
                self.deployment_steps.append(step)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Canary deployment failed: {e}")
            return False
    
    def _execute_deployment_step(self, step: str) -> bool:
        """Execute individual deployment step"""
        try:
            # Simulate deployment step execution
            # In a real implementation, this would contain actual deployment logic
            
            if step == "pull_container_image":
                image = self.deployment_config.get('container', {}).get('image')
                self.logger.info(f"Pulling container image: {image}")
                # subprocess.run(['docker', 'pull', image], check=True)
                
            elif step == "update_configuration":
                self.logger.info("Updating application configuration")
                # Update configuration files, environment variables, etc.
                
            elif step == "deploy_new_version":
                self.logger.info("Deploying new application version")
                # Deploy the new version using container orchestration
                
            elif step == "health_check_new_version":
                self.logger.info("Performing health check on new version")
                # Check application health endpoints
                
            # Add more step implementations as needed
            
            # Simulate execution time
            time.sleep(2)
            return True
            
        except Exception as e:
            self.logger.error(f"Step execution failed: {step} - {e}")
            return False
    
    def post_deployment_checks(self) -> bool:
        """Perform post-deployment validation"""
        try:
            self.logger.info("Performing post-deployment checks...")
            
            # Check application health
            if not self._check_application_health():
                raise DeploymentError("Application health check failed")
            
            # Verify service availability
            if not self._verify_service_availability():
                raise DeploymentError("Service availability check failed")
            
            # Run smoke tests
            if not self._run_smoke_tests():
                self.logger.warning("Smoke tests failed")
            
            # Validate configuration
            if not self._validate_deployed_configuration():
                self.logger.warning("Configuration validation failed")
            
            self.logger.info("Post-deployment checks completed successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Post-deployment checks failed: {e}")
            return False
    
    def _check_application_health(self) -> bool:
        """Check application health endpoints"""
        try:
            api_config = self.app_config.get('api', {})
            base_url = api_config.get('base_url')
            health_endpoint = api_config.get('endpoints', {}).get('health')
            
            if base_url and health_endpoint:
                health_url = f"{base_url}{health_endpoint}"
                result = subprocess.run(
                    ['curl', '-s', '-f', health_url],
                    capture_output=True,
                    timeout=10
                )
                return result.returncode == 0
            
            return True
        except Exception:
            return False
    
    def _verify_service_availability(self) -> bool:
        """Verify service availability"""
        try:
            # Check if services are responding on expected ports
            networking = self.deployment_config.get('networking', {})
            ports = networking.get('ports', [])
            
            for port_config in ports:
                port = port_config.get('port', 80)
                result = subprocess.run(
                    ['nc', '-z', 'localhost', str(port)],
                    capture_output=True
                )
                if result.returncode != 0:
                    self.logger.warning(f"Service not available on port {port}")
                    return False
            
            return True
        except Exception:
            return False
    
    def _run_smoke_tests(self) -> bool:
        """Run basic smoke tests"""
        try:
            # Implement basic smoke tests
            # This could include API endpoint tests, database connectivity, etc.
            self.logger.info("Running smoke tests...")
            
            # Simulate smoke test execution
            time.sleep(3)
            return True
        except Exception:
            return False
    
    def _validate_deployed_configuration(self) -> bool:
        """Validate deployed configuration"""
        try:
            # Verify that the deployed configuration matches expectations
            self.logger.info("Validating deployed configuration...")
            return True
        except Exception:
            return False
    
    def generate_report(self) -> Dict:
        """Generate deployment report"""
        try:
            end_time = datetime.now()
            duration = end_time - self.start_time
            
            report = {
                'deployment_id': self.deployment_id,
                'start_time': self.start_time.isoformat(),
                'end_time': end_time.isoformat(),
                'duration_seconds': duration.total_seconds(),
                'status': self.deployment_status,
                'application': self.app_config.get('application', {}).get('name', 'unknown'),
                'version': self.app_config.get('application', {}).get('version', 'unknown'),
                'environment': self.app_config.get('application', {}).get('environment', 'unknown'),
                'deployment_strategy': self.deployment_config.get('deployment', {}).get('strategy', 'unknown'),
                'steps_completed': len(self.deployment_steps),
                'steps_failed': len(self.failed_steps),
                'completed_steps': self.deployment_steps,
                'failed_steps': self.failed_steps,
                'dry_run': self.dry_run
            }
            
            # Save report to file
            report_file = Path('logs') / f'deployment-report-{self.deployment_id}.json'
            with open(report_file, 'w') as f:
                json.dump(report, f, indent=2)
            
            self.logger.info(f"Deployment report generated: {report_file}")
            return report
            
        except Exception as e:
            self.logger.error(f"Failed to generate report: {e}")
            return {}
    
    def rollback_deployment(self) -> bool:
        """Rollback to previous deployment"""
        try:
            self.logger.info("Starting deployment rollback...")
            
            # Implement rollback logic based on deployment strategy
            strategy = self.deployment_config.get('deployment', {}).get('strategy', 'rolling')
            
            if strategy == 'rolling':
                return self._rollback_rolling_deployment()
            elif strategy == 'blue-green':
                return self._rollback_blue_green_deployment()
            elif strategy == 'canary':
                return self._rollback_canary_deployment()
            
            return False
            
        except Exception as e:
            self.logger.error(f"Rollback failed: {e}")
            return False
    
    def _rollback_rolling_deployment(self) -> bool:
        """Rollback rolling deployment"""
        try:
            self.logger.info("Rolling back rolling deployment...")
            # Implement rolling deployment rollback logic
            return True
        except Exception:
            return False
    
    def _rollback_blue_green_deployment(self) -> bool:
        """Rollback blue-green deployment"""
        try:
            self.logger.info("Rolling back blue-green deployment...")
            # Implement blue-green deployment rollback logic
            return True
        except Exception:
            return False
    
    def _rollback_canary_deployment(self) -> bool:
        """Rollback canary deployment"""
        try:
            self.logger.info("Rolling back canary deployment...")
            # Implement canary deployment rollback logic
            return True
        except Exception:
            return False

def parse_arguments():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description='DevOps Deployment Automation Script',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --config config/
  %(prog)s --config config/ --dry-run
  %(prog)s --config config/ --verbose --rollback
        """
    )
    
    parser.add_argument(
        '--config',
        type=str,
        default='config',
        help='Path to configuration directory (default: config)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Execute in dry-run mode (no actual changes)'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    parser.add_argument(
        '--rollback',
        action='store_true',
        help='Rollback to previous deployment'
    )
    
    parser.add_argument(
        '--report-only',
        action='store_true',
        help='Generate report without executing deployment'
    )
    
    return parser.parse_args()

def main():
    """Main function - orchestrate the deployment process"""
    try:
        # Parse command-line arguments
        args = parse_arguments()
        
        # Set logging level based on verbosity
        if args.verbose:
            logging.getLogger().setLevel(logging.DEBUG)
        
        print("🚀 Starting DevOps Deployment Automation")
        print("=" * 50)
        
        # Initialize deployment manager
        deployment_manager = DeploymentManager(
            config_path=args.config,
            dry_run=args.dry_run
        )
        
        # Handle rollback request
        if args.rollback:
            print("🔄 Executing deployment rollback...")
            success = deployment_manager.rollback_deployment()
            if success:
                print("✅ Rollback completed successfully!")
                sys.exit(0)
            else:
                print("❌ Rollback failed!")
                sys.exit(1)
        
        # Load configuration
        print("📋 Loading configuration files...")
        if not deployment_manager.load_configuration():
            print("❌ Configuration loading failed!")
            sys.exit(1)
        
        # Generate report only if requested
        if args.report_only:
            print("📄 Generating deployment report...")
            report = deployment_manager.generate_report()
            print(f"Report generated: {json.dumps(report, indent=2)}")
            sys.exit(0)
        
        # Validate prerequisites
        print("🔍 Validating prerequisites...")
        if not deployment_manager.validate_prerequisites():
            print("❌ Prerequisites validation failed!")
            sys.exit(1)
        
        # Pre-deployment checks
        print("✅ Performing pre-deployment checks...")
        if not deployment_manager.pre_deployment_checks():
            print("❌ Pre-deployment checks failed!")
            sys.exit(1)
        
        # Execute deployment
        print("🚀 Executing deployment...")
        if not deployment_manager.execute_deployment():
            print("❌ Deployment execution failed!")
            
            # Attempt automatic rollback on failure
            print("🔄 Attempting automatic rollback...")
            if deployment_manager.rollback_deployment():
                print("✅ Automatic rollback completed")
            else:
                print("❌ Automatic rollback failed")
            
            sys.exit(1)
        
        # Post-deployment checks
        print("🔍 Performing post-deployment checks...")
        if not deployment_manager.post_deployment_checks():
            print("⚠️ Post-deployment checks failed, but deployment completed")
        
        # Generate deployment report
        print("📄 Generating deployment report...")
        report = deployment_manager.generate_report()
        
        print("✅ Deployment completed successfully!")
        print(f"📊 Deployment ID: {deployment_manager.deployment_id}")
        print(f"⏱️ Duration: {report.get('duration_seconds', 0):.2f} seconds")
        print(f"📈 Steps completed: {report.get('steps_completed', 0)}")
        
        if args.dry_run:
            print("🔍 This was a dry run - no actual changes were made")
        
    except KeyboardInterrupt:
        print("\n⚠️ Deployment interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"❌ Deployment failed with unexpected error: {e}")
        logging.exception("Unexpected error during deployment")
        sys.exit(1)

if __name__ == "__main__":
    main()
