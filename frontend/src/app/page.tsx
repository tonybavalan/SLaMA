"use client"
import BarSort from "./components/BarSort";
import Donut from "./components/Donut";
import PieChart from "./components/PieChart";
import { barDataSet, columnData, dataSet } from "./helpers/dataset";
import Column from "./components/Column";
import Line from "./components/Line";

export default function Home() {
  return (
    <main className="">
      <div className=" flex items-center mt-2 pl-20 pr-20">
        <PieChart data={dataSet} />
        <Donut data={dataSet} />
      </div>
      <div className="flex justify-between mt-4 pl-20 pr-20">
        <BarSort data={barDataSet}/>
        <Column data={columnData}/>
      </div>
      <div className="mt-4 pl-20 mb-8">
        <Line/>
      </div>
    </main>
  );
}
