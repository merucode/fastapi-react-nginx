import { useState } from 'react';

import GraphSearchForm from '../../components/GraphSearchForm';
import GraphDataList from '../../components/GraphDataList';
import GraphLine from '../../components/GraphLine';
import GraphPie from '../../components/GraphPie';

function GraphPage() {
	const [items, setItems] = useState([]);
	const [comWords,setComWords] = useState([]);

	const handleSubmitSuccess = (res) => {
		setItems(res.data);
		setComWords(res.comWords);
	};

	return (
	<div>
		<h1>GraphPage</h1>
		<GraphSearchForm onSubmitSuccess={handleSubmitSuccess} />
        <GraphLine items={items} comWords={comWords} />
        <GraphPie comWords={comWords} />
        <GraphDataList items={items} comWords={comWords} />
    </div>
	)
}

export default GraphPage;
