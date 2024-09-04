import {useState} from "react";
import { useFormik } from 'formik';
import * as Yup from 'yup';

function RentalForm({ handleNewRental }) {
  const formik = useFormik({
    initialValues: {
      year: '',
      make: '',
      model: '',
    },
    validationSchema: Yup.object({
      year: Yup.string().required('Year is required'),
      make: Yup.string().required('Make is required'),
      model: Yup.string().required('Model is required'),
    }),
    onSubmit: (values) => {
      const formData = {
        year: values.year,
        make: values.make,
        model: values.model,
      };

      fetch('http://127.0.0.1:5555/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      })
        .then((response) => response.json())
        .then((newItem) => handleNewRental(newItem));
    },
  });

  return (
    <div>
      <h2>New Rental:</h2>
      <form className="formClass" onSubmit={formik.handleSubmit}>
        <label>Year:</label>
        <input
          type="text"
          name="year"
          value={formik.values.year}
          onChange={formik.handleChange}
        />
        {formik.errors.year && formik.touched.year && (
          <div>{formik.errors.year}</div>
        )}

        <label>Make:</label>
        <input
          type="text"
          name="make"
          value={formik.values.make}
          onChange={formik.handleChange}
        />
        {formik.errors.make && formik.touched.make && (
          <div>{formik.errors.make}</div>
        )}

        <label>Model:</label>
        <input
          type="text"
          name="model"
          value={formik.values.model}
          onChange={formik.handleChange}
        />
        {formik.errors.model && formik.touched.model && (
          <div>{formik.errors.model}</div>
        )}

        <button type="submit">Add Rental</button>
      </form>
    </div>
  );
}

export default RentalForm;