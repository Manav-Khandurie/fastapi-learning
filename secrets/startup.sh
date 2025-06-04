#!/bin/bash

echo "PRIVATE KEY GENERATION"
openssl genrsa --out secrets/private.pem 2048

echo "Public Key Generation"
openssl rsa -in secrets/private.pem -pubout -out secrets/public.pem