// api.js
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const baseApi = createApi({
  reducerPath: 'baseApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://192.168.100.33:8000/api/' }), // Ajusta la URL de la API según tu configuración
  endpoints: (builder) => ({
    getHumidity: builder.query({
      query: () => 'humidity/'
    }),
    getTemperature: builder.query({
      query: () => 'temperature/'      
    }),
  })
});

export const { useGetHumidityQuery, useGetTemperatureQuery } = baseApi;