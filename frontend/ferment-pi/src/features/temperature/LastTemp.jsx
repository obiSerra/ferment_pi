import React from "react";
import { useSelector } from "react-redux";
import { selectLastTemp } from "./temperatureSlice";

export default function LastTemp() {
  const lastTemp = useSelector(selectLastTemp);

  return <div>Last temperature: {lastTemp?.temperature} C</div>;
}
