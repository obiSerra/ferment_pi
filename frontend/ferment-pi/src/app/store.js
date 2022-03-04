import { configureStore } from '@reduxjs/toolkit';
import temperatureReducer from '../features/temperature/temperatureSlice';

export const store = configureStore({
  reducer: {
    temperature: temperatureReducer,
  },
});
