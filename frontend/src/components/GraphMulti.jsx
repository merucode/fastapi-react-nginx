import React, { PureComponent } from 'react';
import { ResponsiveContainer, ComposedChart, Line, Area, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

function GraphMulti({ items, comWords, stockCode }) {
	const colors = ["#FF0060", "#0079FF", "#00DFA2", "#FFE79B", "#FF8400","#DD58D6", "#080202", "#40128B"]

	// Modify for multi graph
	const BarGraphs = comWords.map((comWord, i) => (
		<Bar yAxisId="left" type="monotone" dataKey={comWord[0]} fill={colors[i]} barSize={20} />
	));

	return (
	<div style={{ width: '70%', height: 300 }}>
    <ResponsiveContainer>
		<ComposedChart
		width={500}
		height={400}
		data={items}
		margin={{
			top: 20,
			right: 20,
			bottom: 20,
			left: 20,
		}}
		>
		<CartesianGrid stroke="#f5f5f5" />
		<XAxis dataKey="date" scale="band" />
		<YAxis yAxisId="left" />
		<YAxis yAxisId="stock" orientation="right" />
    	<YAxis yAxisId="KOSPI" orientation="right" />
		<Tooltip />
		<Legend />
		<Area yAxisId="KOSPI" type="monotone" dataKey="KOSPI" fill="#408E91" stroke="#408E91" fillOpacity={0.03} />
		<Area yAxisId="stock" type="monotone" dataKey={stockCode} fill="#C04A82" stroke="#C04A82" fillOpacity={0.03} />
		{BarGraphs}	// Modify for multi graph
		</ComposedChart>
	</ResponsiveContainer>
	</div>
	);
}

export default GraphMulti;
