<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-10">
                <form method="get" action="/search" ref="form">
                    <div class="search-form">
                        <span class="search-form__icon">
                            <img :src="getStaticImagePath('img/icons/small/search.svg')" alt="Поиск чая">
                        </span>
                        <input class="search-form__input"
                               type="text"
                               maxlength="50"
                               spellcheck="false"
                               required
                               name="q"
                               autocomplete="off"
                               v-model="searchValue"
                               placeholder="Начните поиск"
                               @input="handleChange"
                               title="Введите название или описание чая">
                        <div class="search-form__checkbox">
                            <input type="checkbox"
                                   class="checkbox-input"
                                   id="defaultCheck1"
                                   :checked="isCheckedStock"
                                   name="in_stock">
                            <label class="checkbox-label" for="defaultCheck1">
                                В наличии
                            </label>
                        </div>
                    </div>

                    <button class="search-form__submit" type="submit">
                        <span class="search-form__submit-label">Найти</span>
                    </button>
                </form>

                <ul class="suggest-list" v-show="suggestions.length" style="z-index: 9999">
                    <li v-for="item in suggestions"
                        @click="handleSuggestClick($event, item.title)"
                        class="suggest-list__item">
                        <span>{{item.title}}</span>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "SearchForm",

        mixins: [],

        props: {
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
            }
        },

        methods: {
            handleChange() {
                if (!this.searchValue.length) {
                    this.suggestions = [];
                    return
                }

                window.axios.get('/suggestions', {params: {q: this.searchValue}}).then(response => {
                    this.suggestions = response.data.data.map(item => item);
                })
            },

            handleSuggestClick(e, value) {
                this.searchValue = value;
                this.$refs.form.submit()
            }
        },

        created() {
        }
    }
</script>

<style scoped>

</style>