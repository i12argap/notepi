if (window.django !== undefined) {
    jQuery = window.$ = django.jQuery.noConflict(true) || jQuery;
}
