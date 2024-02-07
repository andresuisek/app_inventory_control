import React, { useEffect, useState } from 'react';
import CustomTable from './CustomTable';
import { useGetInventoryQuery, useGetInventoryHistoricalQuery } from '../baseApi';
import LegosIcon from '../images/legos.png';
import { Col, Row, Tag } from 'antd';
import Title from 'antd/es/typography/Title';

import { Slider } from 'antd';
import { ToastContainer, toast } from 'react-toastify';

const Legos = () => {
    const [toastId, setToastId] = useState(null);
    const [quantityLego, setQuantityLego] = useState(null);
    const { data: dataLego } = useGetInventoryQuery(undefined, {
      pollingInterval: 3000,
    });

    const { data, error, isLoading } = useGetInventoryHistoricalQuery(undefined, {
      pollingInterval: 3000,
    });    

    useEffect(() => {
      var newValue = false;
        
        if(!dataLego)
          return

        if(quantityLego === null){
          setQuantityLego(dataLego[0]?.product_quantity)
          return
        }else{
          if(dataLego[0]?.product_quantity !== quantityLego)
            setQuantityLego(dataLego[0]?.product_quantity)
            newValue = true
        }

        if(newValue){
            if (toastId) {
              toast.dismiss(toastId);
            }

            const newToastId = toast.info('Nuevo valor en el inventario!', {
                  position: "top-left",
                  autoClose: 5000,
                  hideProgressBar: false,
                  closeOnClick: true,
                  pauseOnHover: true,
                  draggable: true,
                  progress: undefined,
                  theme: "light",
              });

            setToastId(newToastId);
          }          
    }, [dataLego]);

    const columns = [
        {
            title: 'Value',
            dataIndex: 'date',
            key: 'date',
        },
        {
            title: 'Quantity',
            dataIndex: 'quantity',
            key: 'quantity'            
          },
        {
            title: 'Registro',
            dataIndex: 'type_register',
            key: 'type_register',
            render: (value) => {
              let color = 'green';
          
              if (value === 'Exit') {
                color = 'volcano';
              }
          
              return (
                <span>
                  <Tag color={color} key={value}>
                    {value}
                  </Tag>
                </span>
              );
            },
        },
    ]

    return (
        <>
            <Row>
                <Col span={24} style={{textAlign: 'center'}}>
                    <Title>Legos Inventory</Title>    
                </Col>
                <Col span={24} style={{display: 'flex', justifyContent: 'center'}}>
                    <img src={LegosIcon} alt='icon' style={{'width': '15%'}} />
                    <Title>{dataLego && `${dataLego[0]?.product_quantity} Units`}</Title>
                </Col>
                <Col span={24}>
                    <CustomTable data={data} isLoading={isLoading} defaultColumns={columns}/>
                </Col>
            </Row>   

            <ToastContainer />
        </>
    );
};

export default Legos;