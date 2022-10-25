#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PasswordConfirmationError(Exception):
    pass

class ServiceNotFound(Exception):
    pass

class UsernameNotFound(Exception):
    pass

class PasswordNotFound(Exception):
    pass

class ServiceAlreadyExists(Exception):
    pass

class AuthenticationFaild(Exception):
    pass
