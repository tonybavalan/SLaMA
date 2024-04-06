import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import { useEffect } from "react";
import { DataProps } from "@/app/helpers/interface";

const Donut: React.FC<DataProps> = ({ data }) => {

    useEffect(() => {
        am4core.useTheme(am4themes_animated);

        let chart = am4core.create("donutchartdiv", am4charts.PieChart3D);
        chart.hiddenState.properties.opacity = 0; // this creates initial fade-in

        chart.legend = new am4charts.Legend();
        chart.data = data;
        chart.innerRadius = 100;

        let series = chart.series.push(new am4charts.PieSeries3D());
        series.dataFields.value = Object.keys(data[0])[1];
        series.dataFields.category = Object.keys(data[0])[0];
    }, [data])

    return (
        <>
            <div id="donutchartdiv" style={{ width: '50%', height: '450px',  border: '1px solid #ccc', borderRadius: '12px', marginTop: '8px'}}></div>
        </>
    )
}

export default Donut;