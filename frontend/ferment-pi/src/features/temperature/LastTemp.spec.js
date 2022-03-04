import { render } from "@testing-library/react";
import React from "react";
import { Provider } from 'react-redux';
import { store } from "../../app/store";
import LastTemp from "./LastTemp";

describe("LastTemp", () => {
  it('has "Last temperature" label', () => {
    const { getByText } = render(
      <Provider store={store}>
        <LastTemp />
      </Provider>
    );

    expect(getByText(/Last temperature/i)).toBeInTheDocument();
  });
});
