import { useState, useEffect, useCallback } from 'react';
import { getItems } from '../../api';
import useAsync from '../../hooks/useAsync';

function HomePage() {
	const [items, setItems] = useState([]);
    const [isLoading, loadingError, getItemsAsync] = useAsync(getItems);

	const loadItems = useCallback(async () => {
		const result = await getItemsAsync();
        setItems([...result]);
	}, [getItemsAsync]);	

    useEffect(() => {
        loadItems();
    }, []);

    return (
    <div>
	    <h1>HomePage</h1>
	    <div>Data From Backend : </div>
        <ol>{items.map((e) => <li key={e.id}>{e.name} {e.date} {e.value}</li>)}</ol>
        <div>{isLoading && <span>Loading</span>}</div>
        <div>{loadingError?.message && <span>{loadingError.message}</span>}</div>
    </div>
    );
}
export default HomePage;
