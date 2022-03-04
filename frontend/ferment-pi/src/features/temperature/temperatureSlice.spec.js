import temperatureReducer from "./temperatureSlice";

describe("counter reducer", () => {
  it("should handle initial state", () => {
    expect(temperatureReducer(undefined, { type: "unknown" })).toEqual({
      lastTemp: null,
      status: "idle",
    });
  });
});
