import React, { PureComponent } from 'react';
import { useSearchParams } from 'react-router-dom';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

function GraphLine({ items, comWords }) {
  const colors = ["#FF0060", "#0A6EBD", "#00DFA2", "#884A39", "#FFC26F", "#080202", "#40128B"]
  const lineGraphs = comWords.map((comWord, i) => (
    <Line type="monotone" dataKey={comWord[0]} stroke={colors[i]} activeDot={{ r: 8 }} />
  ));

  return (
      <>
      <LineChart
        width={500}
        height={300}
        data={items}
        margin={{
          top: 5,
          right: 30,
          left: 20,
          bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Legend />
          {lineGraphs}
      </LineChart>
      </>
  );
}

export default GraphLine;
