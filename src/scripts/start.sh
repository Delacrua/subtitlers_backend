#!/bin/bash

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
