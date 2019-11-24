# -*- coding: utf-8 -*-
from odoo import http

# class ProjectOnPo(http.Controller):
#     @http.route('/project_on_po/project_on_po/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_on_po/project_on_po/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_on_po.listing', {
#             'root': '/project_on_po/project_on_po',
#             'objects': http.request.env['project_on_po.project_on_po'].search([]),
#         })

#     @http.route('/project_on_po/project_on_po/objects/<model("project_on_po.project_on_po"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_on_po.object', {
#             'object': obj
#         })