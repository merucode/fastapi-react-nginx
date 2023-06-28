import { BACKEND_GRAPH_URL } from "./urls";
import axios from "axios";

export async function getItems({ stockCode, startDate, stopDate, reqCount }) {
  const req_config = {
			headers: {
			    "Content-type": "application/json",
		    },
		} 

  const response = await axios.get(
	BACKEND_GRAPH_URL,
	{params: {
			stockCode: stockCode,
			startDate: startDate,
			stopDate: stopDate,
			reqCount: reqCount,
			}
	},	
	req_config
  );
  
  return response.data;
}

