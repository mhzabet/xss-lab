from django.urls import path
from . import views

app_name='vulns'
urlpatterns = [
    path("", views.home_view, name="home"),
    path("xss-no-protection", views.xss_no_protection_view, name="xss-no-protection"),
    path("xss-brackets-protection", views.xss_brackets_protection_view, name="xss-brackets-protection"),
    path("xss-attributes-no-protection", views.xss_attributes_no_protection_view, name="xss-attributes-no-protection"),
    path("xss-javascript-context-no-protection", views.xss_javascript_context_no_protection_view, name="xss-javascript-context-no-protection"),
    path("xss-javascript-context-brackets-escape", views.xss_javascript_context_brackets_escape_view, name="xss-javascript-context-brackets-escape"),
    path("stored-xss-no-protection", views.stored_xss_no_protection_view, name="stored-xss-no-protection"),
    path("dom-xss-no-protection", views.dom_xss_no_protection_view, name="dom-xss-no-protection"),
    path("postmessage-xss-no-protection", views.postmessage_xss_no_protection_view, name="postmessage-xss-no-protection"),
    path("dom-xss-dompurify-bypass", views.dom_xss_dompurify_bypass_view, name="dom-xss-dompurify-bypass")


]
