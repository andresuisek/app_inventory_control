// api.js
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const baseApi = createApi({
  reducerPath: 'baseApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://192.168.100.33:8000/api/' }), // Ajusta la URL de la API según tu configuración
  endpoints: (builder) => ({
    getInventory: builder.query({
      query: () => 'inventory/'
    }),
    getInventoryHistorical: builder.query({
      query: () => 'inventory_historical/'
    }),
    // getTemperature: builder.query({
    //   query: () => 'temperature/'      
    // }),
  })
});

export const { useGetInventoryQuery, useGetInventoryHistoricalQuery } = baseApi;