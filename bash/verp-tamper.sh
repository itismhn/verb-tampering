#!/bin/bash
echo 'testing '$1
for method in GET POST PUT DELETE HEAD OPTIONS PATH TRACE CONNECT; do
    echo $method $(curl -s $1 -X $method -o /dev/null -w ' %{http_code} - %{size_download}')
    done