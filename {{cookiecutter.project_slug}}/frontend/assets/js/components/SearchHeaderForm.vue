<template>
    <div class="search">
        <form class="search-form" method="get" :action="action" ref="form">
            <input class="search-form__input search-form__input_pl"
                   title="Введите название или описание чая"
                   type="text"
                   maxlength="50"
                   spellcheck="false"
                   name="q"
                   autocomplete="off"
                   placeholder="Начните поиск. Например, «улун»"
                   v-model="searchValue"
                   @input="handleChange"
                   @focus="handleFocus"
                   @blur="handleBlur">

            <button class="search-form__button" type="submit">
                <span class="search-form__button-icon">
                    <i class="fas fa-search"></i>
                </span>
            </button>
        </form>

        <transition name="fade">
            <ul class="search-form__suggest-list" v-show="isOpen">
                <li v-for="item in suggestions"
                    @click="handleSuggestClick($event, item)"
                    class="search-form__suggest-item">
                    <span v-html="item.value"></span>
                </li>
            </ul>
        </transition>
    </div>
</template>

<script>
    export default {
        name: "SearchFormHeader",

        mixins: [],

        props: {
            action: {
                type: String,
                required: true,
            },

            inStock: {
                type: String,
                required: false,
            },

            query: {
                type: String,
                required: false,
            }
        },

        computed: {
            isCheckedStock() {
                return this.inStock === 'True'
            }
        },

        data() {
            return {
                searchValue: this.query,
                suggestions: [],
                isOpen: false,
            }
        },

        methods: {
            handleChange() {
                if (!this.searchValue.length) {
                    this.suggestions = [];
                    this.isOpen = false;
                    return
                }

                window.axios.get('/suggestions', {params: {q: this.searchValue}}).then(response => {
                    this.suggestions = response.data.data.map(item => item);
                    this.isOpen = true;
                })
            },

            handleFocus(e) {
                if (this.suggestions.length > 0) {
                    this.isOpen = true;
                }
            },

            handleBlur(e) {
                setTimeout(() => {
                    this.isOpen = false;
                }, 100);
            },

            handleSuggestClick(e, suggestion) {
                this.isOpen = false;

                if (suggestion.is_searchable) {

                    this.searchValue = suggestion.value;
                }

                setTimeout(() => {
                    this.$refs.form.submit()
                }, 1)
            }
        },

        created() {
        }
    }
</script>

<style>
    .fade-enter-active, .fade-leave-active {
        transition: opacity .5s;
    }

    .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
    {
        opacity: 0;
    }
</style>