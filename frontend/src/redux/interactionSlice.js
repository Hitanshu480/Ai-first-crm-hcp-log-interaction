import { createSlice } from "@reduxjs/toolkit";

const interactionSlice = createSlice({
  name: "interaction",
  initialState: {},
  reducers: {
    setInteraction: (state, action) => {
      return action.payload;
    },
  },
});

export const { setInteraction } = interactionSlice.actions;
export default interactionSlice.reducer;

