'''
File: middleware.py
Created Date: Monday March 10th 2025 05:41:21
Author: ristoxxx@github.com
-----
Last Modified: Monday March 10th 2025 06:08:44
Modified By: ristoxxx@github.com
-----
Copyright (c) 2025 ristoxxx@github.com
'''

from django.utils.deprecation import MiddlewareMixin

class CSPMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Content-Security-Policy'] = (
            "default-src 'self'; "  # Salli kaikki resurssit vain samasta domainista
            "frame-ancestors 'self' https://flip-book-tau.vercel.app/; "  # Salli iframe-upotus vain tästä osoitteesta
            "script-src 'self' 'unsafe-inline'; "  # Salli omat skriptit ja inline-skriptit
            "style-src 'self' 'unsafe-inline'; "  # Salli omat tyylit ja inline-tyylit
            "img-src 'self' data:; "  # Salli omat kuvat ja data-URI:t
            "connect-src 'self'; "  # Salli AJAX/FETCH-pyynnöt vain omaan domainiin
        )
        return response
