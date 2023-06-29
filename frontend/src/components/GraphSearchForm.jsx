import { useEffect, useState, useCallback } from 'react';

import { getItems } from '../api';
import useAsync from '../hooks/useAsync';

function GraphSearchForm({ onSubmitSuccess }) {
	const [stockCode, setStockCode] = useState("000001");
	const [startDate, setStartDate] = useState("2023-06-01");
	const [stopDate, setStopDate] = useState("2023-06-06");
	const [reqCount, setReqCount] = useState(4);
	
	const [isLoading, loadingError, getItemsAsync] = useAsync(getItems);

	const loadItems = useCallback(async(options) => {
        const result = await getItemsAsync(options);
		return result;
	}, [getItemsAsync]);

	const submitHandler = async (e) => {
		e.preventDefault();
        const result = await loadItems({ stockCode, startDate, stopDate, reqCount });
		if (!result) return;
		onSubmitSuccess(result, stockCode);
	};

	return (
	  <div>
		<form onSubmit={submitHandler}>
			<div>
				<label htmlFor="stockCode">stockcode</label>
				<input type="text" id="stockCode" name="stockCode"
				value={stockCode} onChange={(e) => setStockCode(e.target.value)}/>
			</div>
			<div>
				<label htmlFor="startDate">startdate</label>
				<input type="date" id="startDate" name="startDate"
				value={startDate} onChange={(e) => setStartDate(e.target.value)}/>
			</div>
			<div>
				<label htmlFor="stopDate">stopdate</label>
				<input type="date" id="stopDate" name="stopDate"
				value={stopDate} onChange={(e) => setStopDate(e.target.value)}/>
			</div>
			<div>
				<label htmlFor="reqCount">reqCount</label>
				<input type="number" id="reqCount" name="reqCount"
				value={reqCount} onChange={(e) => setReqCount(e.target.value)}/>
			</div>
			<button type="submit">Search</button>
		</form>
	    {isLoading && <span>Loading</span>}
		{loadingError?.message && <span>{loadingError.message}</span>}
	  </div>
	);
}

export default GraphSearchForm;
