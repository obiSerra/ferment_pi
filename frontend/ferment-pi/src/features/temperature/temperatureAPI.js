import axios from "axios";
const url = "http://127.0.0.1:8000/api/temperature";
export function fetchLastTemperature() {
  return axios
    .get(url)
    .catch(function (error) {
      console.log(error);
      return {};
    });
}
