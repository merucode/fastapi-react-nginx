import { BACKEND_DB_TEST_URL } from "./urls";
import axios from "axios";

export async function getItems() {
  const req_config = {
            headers: {
                "Content-type": "application/json",
            },
        } 

  const response = await axios.get(
    BACKEND_DB_TEST_URL,
    req_config
  )
 
  return response.data;
}
