import ListGroup from "./components/ListGroup";

let items = [
  'New York', 
  'San Jose', 
  'Tokyo',
  'Hongkong',
  'Rexburg', 
  'Santa Cruz'
];

const handleSelectedItem = (item:string) => {
  console.log(item);
}
function App() {
  return <div> <ListGroup items={items} heading='Cities' onSelectItem={handleSelectedItem}/> </div>;
}

export default App;
