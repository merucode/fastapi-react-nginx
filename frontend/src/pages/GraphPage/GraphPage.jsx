import { useState } from 'react';

import GraphSearchForm from '../../components/GraphSearchForm';
import GraphMulti from '../../components/GraphMulti';
import GraphPie from '../../components/GraphPie';

function GraphPage() {
	const [items, setItems] = useState([]);
	const [comWords,setComWords] = useState([]);
    const [code, setCode] = useState('');

	const handleSubmitSuccess = (res, stockCode) => {
		setItems(res.data);
		setComWords(res.comWords);
        setCode(stockCode)
	};

	return (
	<div>
		<h1>GraphPage</h1>
		<GraphSearchForm onSubmitSuccess={handleSubmitSuccess} />
        <GraphMulti items={items} comWords={comWords} stockCode={code}/>
        <GraphPie comWords={comWords} />
    </div>
	)
}

export default GraphPage;
