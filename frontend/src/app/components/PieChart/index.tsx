import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import { useEffect } from "react";
import { DataProps } from "@/app/helpers/interface";


const PieChart:React.FC<DataProps> = ({data}) => {

    useEffect(() => {
        am4core.useTheme(am4themes_animated);
     
        let Chart = am4core.create("piechartdiv", am4charts.PieChart);

        Chart.data = data;

        // Add and configure Series
        let pieSeries = Chart.series.push(new am4charts.PieSeries());
        pieSeries.dataFields.value = Object.keys(data[0])[1];
        pieSeries.dataFields.category =  Object.keys(data[0])[0];
        pieSeries.slices.template.stroke = am4core.color("#fff");
        pieSeries.slices.template.strokeOpacity = 1;

        // This creates initial animation
        pieSeries.hiddenState.properties.opacity = 1;
        pieSeries.hiddenState.properties.endAngle = -90;
        pieSeries.hiddenState.properties.startAngle = -90;

        Chart.hiddenState.properties.radius = am4core.percent(0);
    }, [data])

    return (
        <>
            <div id="piechartdiv" style={{ width: '50%', height: '400px', border: '1px solid #ccc', borderRadius: '12px' }}></div>
        </>
    )
}

export default PieChart;
