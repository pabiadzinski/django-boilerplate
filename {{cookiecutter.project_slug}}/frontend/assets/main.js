import Vue from 'vue';

window.axios = require('axios').default;

import './style/app.scss';

console.info("run app");

// global mixin
import DjangoMixin from './js/mixins/django';
Vue.mixin(DjangoMixin);

import StarRating from 'vue-star-rating'
Vue.component('star-rating', StarRating);

// Vue.component('search-form', require('./js/components/SearchForm.vue').default);
Vue.component('search-header-form', require('./js/components/SearchHeaderForm.vue').default);
Vue.component('price-history', require('./js/components/PriceHistory.vue').default);
Vue.component('comment-form', require('./js/components/CommentForm.vue').default);

window.getCookie = function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

window.TOKEN_NAME = 'csrftoken';

axios.defaults.headers.common['X-CSRFToken'] = getCookie(TOKEN_NAME);

var app = new Vue({
    el: '#page-container',
    data: {},
});


