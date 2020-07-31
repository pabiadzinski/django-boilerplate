<template>
    <div class="container">
        <textarea v-model="text"></textarea>

        <star-rating :star-size="30" :rating="rating" @rating-selected="rating = $event"></star-rating>

        <button type="submit" @click.prevent="handleSubmit">Отправить</button>
    </div>
</template>

<script>
    export default {
        name: "CommentForm",

        components: {},

        mixins: [],

        props: {
            url: {
                type: String,
                required: false,
            },
        },

        computed: {},

        data() {
            return {
                text: null,
                rating: null,
            }
        },

        methods: {
            handleSubmit() {
                const form = Object.assign({}, {text: this.text, rating: this.rating});

                window.axios.post(this.url, form).then(response => {
                    console.log(response);
                })
            },
        },

        created() {
        }
    }
</script>

<style scoped>

</style>