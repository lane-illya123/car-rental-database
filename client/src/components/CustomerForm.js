import {useState} from "react";
import { useFormik } from 'formik';
import * as Yup from 'yup';


function CustomerForm({handleNewCustomer}){

  const formik = useFormik({
    initialValues: {
      first_name: '',
      last_name: '',
    },
    validationSchema: Yup.object({
      first_name: Yup.string().required('First Name is required'),
      last_name: Yup.string().required('Last Name is required'),
    }),
    onSubmit: (values) => {
      const formData = {
        first_name: values.first_name,
        last_name: values.last_name
      };

      fetch('/customer', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          
        },
        body: JSON.stringify(formData),
      })
        .then((response) => response.json())
        .then((newCustomer) =>console.log((newCustomer)))
        .catch((error) => console.log('Error:', error));

        console.log('Request Body:', formData);
    },
  });

  return (
    <div>
      <h2>New Customer:</h2>
      <form className="formClass" onSubmit={formik.handleSubmit}>
        <label>First Name:</label>
        <input
          type="text"
          name="first_name"
          value={formik.values.first_name}
          onChange={formik.handleChange}
        />
        {formik.errors.first_name && formik.touched.first_name && (
          <div>{formik.errors.first_name}</div>
        )}

        <label>Last Name:</label>
        <input
          type="text"
          name="last_name"
          value={formik.values.last_name}
          onChange={formik.handleChange}
        />
        {formik.errors.last_name && formik.touched.last_name && (
          <div>{formik.errors.last_name}</div>
        )}

        <button type="submit">Add Customer</button>
      </form>
    </div>
  );
}

export default CustomerForm;