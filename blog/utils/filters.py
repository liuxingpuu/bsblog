# coding:utf-8
import string

def configure_template_filters(app):
    """配置模版过滤器"""
    @app.template_filter()
    def content_split(value):
        result = value.split('</p>')[0]+value.split('</p>')[1]
        return result
