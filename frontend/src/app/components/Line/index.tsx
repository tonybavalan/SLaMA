import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import { useEffect } from "react";

const Line = () => {

    useEffect(() => {
        am4core.useTheme(am4themes_animated);

        let chart = am4core.create("linechartdiv", am4charts.XYChart);

        chart.data = generateChartData();

        let dateAxis = chart.xAxes.push(new am4charts.DateAxis());
        dateAxis.renderer.minGridDistance = 50;

        let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());

        let series = chart.series.push(new am4charts.LineSeries());
        series.dataFields.valueY = "visits";
        series.dataFields.dateX = "date";
        series.strokeWidth = 2;
        series.minBulletDistance = 10;
        series.tooltipText = "{valueY}";
        if (series.tooltip) {
            series.tooltip.pointerOrientation = "vertical";
            series.tooltip.background.cornerRadius = 20;
            series.tooltip.background.fillOpacity = 0.5;
            series.tooltip.label.padding(12, 12, 12, 12)
        }

        // Add scrollbar
        chart.scrollbarX = new am4charts.XYChartScrollbar();
        if (chart.scrollbarX) {
            chart.scrollbarX.series.push(series);
        }

        // Add cursor
        chart.cursor = new am4charts.XYCursor();
        chart.cursor.xAxis = dateAxis;
        chart.cursor.snapToSeries = series;

        function generateChartData() {
            let chartData = [];
            let firstDate = new Date();
            firstDate.setDate(firstDate.getDate() - 1000);
            let visits = 1200;
            for (var i = 0; i < 500; i++) {
                let newDate = new Date(firstDate);
                newDate.setDate(newDate.getDate() + i);

                visits += Math.round((Math.random() < 0.5 ? 1 : -1) * Math.random() * 10);

                chartData.push({
                    date: newDate,
                    visits: visits
                });
            }
            return chartData;
        }
    })
    return (
        <>
            <div id="linechartdiv" style={{ width: '47%', height: '400px', border: '1px solid #ccc', borderRadius: '12px' }}></div>
        </>
    )
}

export default Line;