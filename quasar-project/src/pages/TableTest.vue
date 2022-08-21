
<template>
<form @submit.prevent="updade" class="q-pa-md">
  <div class="q-pa-md q-gutter-sm">

     <q-input
      v-model.number="number"
      type="number"
      style="max-width: 250px"
      label="Порог"
    />
      <q-select
        label="Сравнение"
        filled
        v-model="equal"
        :options="stringEqual"
        style="width: 250px"
        behavior="menu"
      />
      <q-select
        label="Колонка"
        filled
        v-model="columnName"
        :options="stringColumn"
        style="width: 250px"
        behavior="menu"
      />
      <q-btn
        type="submit"
        :loading="submitting"
        label="Отфильтровать"
        class="q-mt-md"
        color="teal"
      />
  </div>
</form>
  <div class="q-pa-md">
    <q-table :rows="rows"
             :columns="columns"
             title="Таблица из задания"
             :filter="filter"
             >
    </q-table>
  </div>

</template>


<script>

import { ref } from 'vue'
import { api } from 'src/boot/axios'


export default{

    data(){

    const submitting = ref(false)

    function  updade(){
      api.get("http://127.0.0.1:5000/?"+"number="+this.number+"&equal="+this.equal+"&column="+this.columnName).then((response) =>{
        console.log(response.data)
        this.rows = response.data
      }).catch((e)=>{console.log(e)})
    }

    return{
      number: ref(),
      equal: ref(),
      columnName:ref(),
      submitting,
      updade,
      stringEqual:['over', 'less', 'equal'],
      stringColumn:['price','weight'],
      rows: [],
      filter: '',
      columns : [
        {
          name:"price",
          label:"Цена",
          field:"price",
          sortable: true,
          align: 'center',
        },
        {
          name:"weight",
          label:"Вес",
          field:"weight",
          sortable: true,
          align: 'center',
        }],

    barChartOption: {
          grid:{
            bottom:'50%'
          },
          legend: {},
          tooltip: {},
          dataset: {
            dimensions: ['price'],
            source: []


          },
          xAxis: {type: 'category',
          axisLabel:{
            rotate:45
          }},
          yAxis: {},
          // Declare several bar series, each will be mapped
          // to a column of dataset.source by default.
          series: [
            {type: 'bar'},
            {type: 'bar'},

          ]
        },

    }
  },
  methods:{
    getTable(){
      this.$axios.get("http://127.0.0.1:5000/?"+"number="+this.number).then((response) =>{
        console.log(response.data)
        this.rows = response.data
      }).catch((e)=>{console.log(e)})
    }
  },
  mounted(){
    this.getTable()
  },
  components: {
    },



}
</script>
