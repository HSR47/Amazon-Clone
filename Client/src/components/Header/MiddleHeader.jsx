import { useEffect, useState } from 'react'
import styles from './Header.module.css'

let dropdownOptions = [
    {value : "all" , label : "All"},
    {value : "laptop" , label : "Laptop"},
    {value : "phone" , label : "Phone"},
    {value : "washing-machine" , label : "Washing Machine"},
]

function MiddleHeader(){
    let [selectedOption , setSelectedOption] = useState(dropdownOptions[0].value)
    let [selectedOptionLabel , setSelectedOptionLabel] = useState(dropdownOptions[0].label)

    function handleOptionChange(e){
        setSelectedOption(e.target.value)
        for (let i of dropdownOptions)
        {
            if (i.value == e.target.value)
            {
                setSelectedOptionLabel(i.label)
                break
            }
        }
    }

    return (
        <div className={styles.middle}>

            <div className={styles.dropdown}>
                <div className={styles.button}>
                    <div className={styles.label}>{selectedOptionLabel}</div>
                    <img src="/dropdown.svg" alt="dropdown" />
                </div>
                <select value={selectedOption} onChange={handleOptionChange}>
                    {dropdownOptions.map(function(i){
                        return <option value={i.value} key={i.value}>{i.label}</option>
                    })}
                </select>
            </div>

            
            <div className={styles.searchInput}>
                <input type="text" placeholder='Search Amazon.in' />
            </div>
            
            
            <div className={styles.searchBtn}>
                <img src="/search.svg" alt="search" />
            </div>
        </div>
    )
}

export default MiddleHeader