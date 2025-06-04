#!/bin/bash

echo "PRIVATE KEY GENERATION"
openssl genrsa --out private.pem 2048

echo "Public Key Generation"
openssl rsa -in private.pem -pubout -out public.pem