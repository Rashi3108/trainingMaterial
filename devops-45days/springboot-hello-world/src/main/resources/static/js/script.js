// Enhanced interactivity for Spring Boot Hello World application

document.addEventListener('DOMContentLoaded', function() {
    // Update timestamp every second
    updateTimestamp();
    setInterval(updateTimestamp, 1000);
    
    // Add form validation
    setupFormValidation();
    
    // Add API testing functionality
    setupApiTesting();
    
    // Add smooth scrolling for navigation
    setupSmoothScrolling();
});

/**
 * Update the timestamp display with current time
 */
function updateTimestamp() {
    const timestampElement = document.querySelector('.timestamp-value');
    if (timestampElement) {
        const now = new Date();
        const formattedTime = now.getFullYear() + '-' + 
                            String(now.getMonth() + 1).padStart(2, '0') + '-' + 
                            String(now.getDate()).padStart(2, '0') + ' ' +
                            String(now.getHours()).padStart(2, '0') + ':' + 
                            String(now.getMinutes()).padStart(2, '0') + ':' + 
                            String(now.getSeconds()).padStart(2, '0');
        timestampElement.textContent = formattedTime;
    }
}

/**
 * Setup form validation for the greeting form
 */
function setupFormValidation() {
    const form = document.querySelector('.greeting-form');
    const nameInput = document.querySelector('#name');
    
    if (form && nameInput) {
        form.addEventListener('submit', function(e) {
            const name = nameInput.value.trim();
            
            if (name.length === 0) {
                e.preventDefault();
                showNotification('Please enter your name', 'error');
                nameInput.focus();
                return;
            }
            
            if (name.length > 50) {
                e.preventDefault();
                showNotification('Name is too long (max 50 characters)', 'error');
                nameInput.focus();
                return;
            }
            
            // Show loading state
            const submitBtn = form.querySelector('.btn-primary');
            if (submitBtn) {
                submitBtn.textContent = 'Updating...';
                submitBtn.disabled = true;
            }
        });
        
        // Real-time validation
        nameInput.addEventListener('input', function() {
            const name = this.value.trim();
            if (name.length > 50) {
                this.style.borderColor = '#ef4444';
                showNotification('Name is too long (max 50 characters)', 'warning');
            } else {
                this.style.borderColor = '#e5e7eb';
            }
        });
    }
}

/**
 * Setup API testing functionality
 */
function setupApiTesting() {
    // Add click handlers to API examples
    const apiExamples = document.querySelectorAll('.api-example code');
    
    apiExamples.forEach(function(codeElement) {
        codeElement.style.cursor = 'pointer';
        codeElement.title = 'Click to test this API endpoint';
        
        codeElement.addEventListener('click', function() {
            const endpoint = this.textContent.trim();
            const fullUrl = window.location.origin + endpoint;
            
            // Show loading notification
            showNotification('Testing API endpoint...', 'info');
            
            // Open in new tab
            window.open(fullUrl, '_blank');
        });
    });
}

/**
 * Setup smooth scrolling for navigation
 */
function setupSmoothScrolling() {
    // Add smooth scroll behavior to the page
    document.documentElement.style.scrollBehavior = 'smooth';
    
    // Add scroll-to-top functionality
    let scrollToTopBtn = document.createElement('button');
    scrollToTopBtn.innerHTML = '↑';
    scrollToTopBtn.className = 'scroll-to-top';
    scrollToTopBtn.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: #4f46e5;
        color: white;
        border: none;
        font-size: 20px;
        cursor: pointer;
        opacity: 0;
        transition: all 0.3s ease;
        z-index: 1000;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
    `;
    
    document.body.appendChild(scrollToTopBtn);
    
    // Show/hide scroll to top button
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollToTopBtn.style.opacity = '1';
        } else {
            scrollToTopBtn.style.opacity = '0';
        }
    });
    
    // Scroll to top functionality
    scrollToTopBtn.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

/**
 * Show notification messages to the user
 * @param {string} message - The message to display
 * @param {string} type - The type of notification (success, error, warning, info)
 */
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(function(notification) {
        notification.remove();
    });
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = 'notification notification-' + type;
    notification.textContent = message;
    
    // Style the notification
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 20px;
        border-radius: 8px;
        color: white;
        font-weight: 500;
        z-index: 1001;
        opacity: 0;
        transform: translateX(100%);
        transition: all 0.3s ease;
        max-width: 300px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    `;
    
    // Set background color based on type
    const colors = {
        success: '#10b981',
        error: '#ef4444',
        warning: '#f59e0b',
        info: '#3b82f6'
    };
    notification.style.backgroundColor = colors[type] || colors.info;
    
    // Add to DOM
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(function() {
        notification.style.opacity = '1';
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Auto remove after 3 seconds
    setTimeout(function() {
        notification.style.opacity = '0';
        notification.style.transform = 'translateX(100%)';
        setTimeout(function() {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }, 3000);
    
    // Allow manual dismissal
    notification.addEventListener('click', function() {
        this.style.opacity = '0';
        this.style.transform = 'translateX(100%)';
        setTimeout(() => {
            if (this.parentNode) {
                this.parentNode.removeChild(this);
            }
        }, 300);
    });
}

// Add some fun easter eggs
document.addEventListener('keydown', function(e) {
    // Konami code easter egg
    const konamiCode = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65];
    if (!window.konamiProgress) window.konamiProgress = 0;
    
    if (e.keyCode === konamiCode[window.konamiProgress]) {
        window.konamiProgress++;
        if (window.konamiProgress === konamiCode.length) {
            showNotification('🎉 Konami Code activated! You found the easter egg!', 'success');
            document.body.style.animation = 'rainbow 2s infinite';
            window.konamiProgress = 0;
            
            // Add rainbow animation
            const style = document.createElement('style');
            style.textContent = `
                @keyframes rainbow {
                    0% { filter: hue-rotate(0deg); }
                    100% { filter: hue-rotate(360deg); }
                }
            `;
            document.head.appendChild(style);
            
            setTimeout(() => {
                document.body.style.animation = '';
            }, 4000);
        }
    } else {
        window.konamiProgress = 0;
    }
});
