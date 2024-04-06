import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import { useEffect } from "react";
import { DataProps } from "@/app/helpers/interface";

const BarSort: React.FC<DataProps> = ({ data }) => {

    useEffect(() => {
        am4core.useTheme(am4themes_animated);

        let chart = am4core.create("barchartdiv", am4charts.XYChart);

        chart.data = data;

        chart.padding(40, 40, 40, 40);

        let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
        categoryAxis.renderer.grid.template.location = 0;
        categoryAxis.dataFields.category = Object.keys(data[0])[0];
        categoryAxis.renderer.minGridDistance = 60;
        categoryAxis.renderer.inversed = true;
        categoryAxis.renderer.grid.template.disabled = true;

        let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
        valueAxis.min = 0;
        valueAxis.extraMax = 0.1;

        let series = chart.series.push(new am4charts.ColumnSeries());
        series.dataFields.categoryX = Object.keys(data[0])[0];
        series.dataFields.valueY = Object.keys(data[0])[1];
        series.tooltipText = "{valueY.value}"
        series.columns.template.strokeOpacity = 0;
        series.columns.template.column.cornerRadiusTopRight = 10;
        series.columns.template.column.cornerRadiusTopLeft = 10;

        let labelBullet = series.bullets.push(new am4charts.LabelBullet());
        labelBullet.label.verticalCenter = "bottom";
        labelBullet.label.dy = -10;
        labelBullet.label.text = "{values.valueY.workingValue.formatNumber('#.')}";

        chart.zoomOutButton.disabled = true;

        series.columns.template.adapter.add("fill", function (fill, target) {
            if (target.dataItem) {
                return chart.colors.getIndex(target.dataItem.index);
            }
        });

        setInterval(function () {
            am4core.array.each(chart.data, function (item) {
                item.visits += Math.round(Math.random() * 200 - 100);
                item.visits = Math.abs(item.visits);
            })
            chart.invalidateRawData();
        }, 2000)

        categoryAxis.sortBySeries = series;
    })
    return (
        <>
            <div id="barchartdiv" style={{ width: '50%', height: '400px', border: '1px solid #ccc', borderRadius: '12px', marginTop: '8px' }}></div>
        </>
    )
}

export default BarSort;