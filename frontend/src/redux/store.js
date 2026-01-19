import { configureStore } from "@reduxjs/toolkit";
import interactionReducer from "./interactionSlice";

export default configureStore({
  reducer: {
    interaction: interactionReducer,
  },
});

