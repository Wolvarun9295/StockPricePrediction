var chartPredictedData;

function requestData() {
    var requests = $.get('/data');
    var tm = requests.done(function (result) {

        var seriesPredictedData = chartPredictedData.series[0],
            shiftPredictedData = seriesPredictedData.data.length > 20;

        var seriesActualData = chartPredictedData.series[1],
            shiftActualData = seriesPredictedData.data.length > 20;

        var data1 = [];

        data1.push(result[0]);
        data1.push(result[1]);

        var data2 = [];
        data2.push(result[0]);
        data2.push(result[2]);

        chartPredictedData.series[0].addPoint(data1, true, shiftPredictedData);
        chartPredictedData.series[1].addPoint(data2, true, shiftActualData);

        $(".sensor1").text("");
        $(".sensor1").text("Prediction: " + data1[1]);

        $(".sensor2").text("");
        $(".sensor2").text("Close: " + data2[1]);

        setTimeout(requestData, 2000);
    });
}

$(document).ready(function () {
    chartPredictedData = Highcharts.stockChart({
        chart:
        {
            renderTo: 'chart',
            defaultSeriesType: 'areaspline',
            zoomType: 'xy',

            events: {
                load: requestData
            }
        },

        rangeSelector: {
            buttons: [
                {
                    type: 'min',
                    count: '1',
                    text: '1Min'
                },
                {
                    type: 'hour',
                    count: '1',
                    text: '1Hr'
                },
                {
                    type: 'day',
                    count: '1',
                    text: '1D'
                },
                {
                    type: 'all',
                    text: 'ALL'
                }],
            selected: 4
        },

        xAxis: {
            type: 'datetime',
            labels: {
                format: '{value:%e-%m-%y %H:%M:%S}'
            },
            tickPixelInterval: 100,
            maxZoom: 100 * 100,
        },

        yAxis: {
            lineWidth: 1,
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Value',
                margin: 20
            },
        },

        series: [{
            color: '#ff0000',
            lineColor: '#000000',
            name: 'Predicted Close',
            data: []
        },
        {
            color: '#0a6ebd',
            lineColor: '#000000',
            name: 'Actual Close',
            data: []
        }],

    });

});
