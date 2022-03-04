import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { fetchLastTemperature } from './temperatureAPI';
const initialState = {
  lastTemp: null,
  status: 'idle',
};

export const lastTempAction = createAsyncThunk(
    'counter/fetchCount',
    async () => {
      const response = await fetchLastTemperature(); 
      return response.data;
    }
  );

export const temperatureSlice = createSlice({
    name: 'temperature',
    initialState: initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder
        .addCase(lastTempAction.pending, (state) => {
          state.status = 'loading';
        })
        .addCase(lastTempAction.fulfilled, (state, action) => {
          state.status = 'idle';
          state.lastTemp = action.payload.temperature;
        });
    }
})

export const selectLastTemp = (state) => state.temperature.lastTemp;

export default temperatureSlice.reducer;