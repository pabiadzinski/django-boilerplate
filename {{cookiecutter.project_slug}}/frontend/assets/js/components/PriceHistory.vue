<script>
    import VueCharts from 'vue-chartjs'
    import {Bar, mixins} from 'vue-chartjs'

    export default {
        name: "PriceHistory",
        mixins: mixins,
        extends: Bar,

        data() {
            return {
                options: {
                    responsive: true,
                    // steppedLine: true,
                    maintainAspectRatio: false,
                    // spanGaps: false,
                    // showLines: false,

                    legend: {
                        position: 'top',
                        display: true,
                        labels: {
                            boxWidth: 12,
                        }
                    },

                    title: {
                        display: true,
                        text: 'Изменения цен',
                    },

                    elements: {
                        line: {
                            // tension: 0.4, // disables bezier curves
                            // pointBackgroundColor: 'white',
                            // pointBorderColor: 'black',
                            borderWidth: 2,

                            // fill: true
                        },

                        point: {
                            // hitRadius: 1,
                            radius: 1,
                            borderWidth: 0,
                            // radius: 1,
                            // pointStyle: 'start',

                            // pointBackgroundColor: 'black',
                            // pointBorderColor: 'black',
                        }
                    },
                    animation: {
                        // onProgress: function () {
                        // }
                    },

                    scales: {
                        yAxes: [{
                            gridLines: {
                                drawBorder: false,
                                color: 'rgba(220,223,230,0.24)'
                            },
                            ticks: {
                                beginAtZero: true
                            }
                        }],
                        xAxes: [{
                            gridLines: {
                                drawBorder: false,
                                color: 'rgba(220,223,230,0.24)'
                            },
                        }],
                    }
                },
                data: {
                    labels: [1, 2,],
                    datasets: [
                        {
                            label: 'GitHub Commits',
                            backgroundColor: '#7EBC42',
                            data: [1, 2,]
                        }
                    ]
                }
            }
        },
        mounted() {
            this.renderChart(this.data, this.options)
        }
    }
</script>