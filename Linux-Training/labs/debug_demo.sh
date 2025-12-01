#!/bin/bash
set -x

num1=10
num2=20

# Bug: wrong variable name
sum=$((num1 + numm2))

echo "Sum = $sum"
set +x