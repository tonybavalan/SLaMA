import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import { useEffect } from "react";
import { DataProps } from "@/app/helpers/interface";

const Column: React.FC<DataProps> = ({ data }) => {

    useEffect(() => {
        am4core.useTheme(am4themes_animated);

        // Create chart instance
        let chart = am4core.create("columnchartdiv", am4charts.XYChart);
        chart.scrollbarX = new am4core.Scrollbar();

        chart.data = data;

        let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
        categoryAxis.dataFields.category = Object.keys(data[0])[0];
        categoryAxis.renderer.grid.template.location = 0;
        categoryAxis.renderer.minGridDistance = 30;
        categoryAxis.renderer.labels.template.horizontalCenter = "right";
        categoryAxis.renderer.labels.template.verticalCenter = "middle";
        categoryAxis.renderer.labels.template.rotation = 270;
        if (categoryAxis.tooltip) {
            categoryAxis.tooltip.disabled = true;
        }
        categoryAxis.renderer.minHeight = 110;

        let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
        valueAxis.renderer.minWidth = 50;

        // Create series
        let series = chart.series.push(new am4charts.ColumnSeries());
        series.sequencedInterpolation = true;
        series.dataFields.valueY = Object.keys(data[0])[1];
        series.dataFields.categoryX = Object.keys(data[0])[0];
        series.tooltipText = "[{categoryX}: bold]{valueY}[/]";
        series.columns.template.strokeWidth = 0;

        if (series.tooltip) {
            series.tooltip.pointerOrientation = "vertical";
        }

        series.columns.template.column.cornerRadiusTopLeft = 10;
        series.columns.template.column.cornerRadiusTopRight = 10;
        series.columns.template.column.fillOpacity = 0.8;

        // on hover, make corner radiuses bigger
        let hoverState = series.columns.template.column.states.create("hover");
        hoverState.properties.cornerRadiusTopLeft = 0;
        hoverState.properties.cornerRadiusTopRight = 0;
        hoverState.properties.fillOpacity = 1;

        series.columns.template.adapter.add("fill", function (fill, target) {
            if (target.dataItem) {
                return chart.colors.getIndex(target.dataItem.index);
            }
        });

        chart.cursor = new am4charts.XYCursor();

    }, [data])

    return (
        <>
            <div id="columnchartdiv" style={{ width: '50%', height: '400px', border: '1px solid #ccc', borderRadius: '12px', marginTop: '8px' }}></div>
        </>
    )
}

export default Column;