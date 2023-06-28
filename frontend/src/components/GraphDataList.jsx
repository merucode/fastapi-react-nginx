function DataListItem({ item, comWords }) {
  return (
    <div>
        <p>{item.date} {comWords.map((e) => <span>{item[e[0]]} </span>)}</p>   
    </div>
  );
}

function GraphDataList({ items, comWords }) {
  return (
    <>
      <ul>
        {items.map((item) => {
          return (
            <li key={item.date}>
              <DataListItem item={item} comWords={comWords}/>
            </li>
          );
        })}
      </ul>

      <ul>
        {comWords.map((comWord) => {
          return (
            <li key={comWord[0]}>comWord : {comWord[0]}, count : {comWord[1]}</li>
          );
        })}
      </ul>
    </>
  );
}

export default GraphDataList;
