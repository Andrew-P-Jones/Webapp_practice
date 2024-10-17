interface Props {
    items:string[];
    heading:string;
    onSelectItem: (item:string) => void;
}


import { useState } from "react";

function ListGroup({items, heading, onSelectItem}:Props) {
    
    const [selectedIndex, setSelectedIndex] = useState(-1);
    return (
    <>
    <h1>{heading}</h1>
    {items.length ===0 && <p>No item found</p>}
    <ul className="list-group">
    {items.map((item, index) => 
    <li 
    className={selectedIndex === index ? 'list-group-item active' : 'list-group-item'} 
    key={item} 
    onClick={() => {setSelectedIndex(index);
        onSelectItem(item);
    }}>
        {item}
        </li>)}
  </ul>
  <p>Please Select your city, once it is highlighted blue press enter</p>
  </>
);
}

export default ListGroup;