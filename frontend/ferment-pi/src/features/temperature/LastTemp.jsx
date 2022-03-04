import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { lastTempAction, selectLastTemp } from "./temperatureSlice";

export default function LastTemp() {
  const lastTemp = useSelector(selectLastTemp);
  
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(lastTempAction());
  }, []);
  return <div>Last temperature: {lastTemp?.temperature} C</div>;
}
