<template>
  <div class="container">
    <div>
      <b-form-select v-model="selected" :options="options"></b-form-select>
      <div class="mt-3">Selected: <strong>{{ selected }}</strong></div>
    </div>
    <b-form>
      <b-form-input v-model="query" placeholder="Enter the file content"></b-form-input>
      <b-col lg="4" class="pb-2">
        <b-button @click="find" variant="primary">Find</b-button>
      </b-col>
    </b-form>
    <div>
      <b-list-group>
        <b-list-group-item button v-for="item in this.relevantDocuments" @click="download(item[1])">{{
            item[1]
          }}
        </b-list-group-item>
      </b-list-group>
      <p>{{ text }}</p>
    </div>

    <div>
      <p>Sugest</p>
      <b-list-group>
        <b-list-group-item button v-for="item in this.expand" @click="find_expand(item)">{{
            item
          }}
        </b-list-group-item>
      </b-list-group>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "find",
  data() {
    return {
      query: '',
      text: '',
      relevantDocuments: [],
      expand: [],
      selected: null,
      options: [
        {value: 'vectorial', text: 'Select the vectorial model'},
        {value: 'booleano', text: 'Select the boolean model'},
      ]
    }
  },
  methods: {
    download(name) {
      console.log(name)
      const data = JSON.stringify({
        "file_name": name,
      });

      const config = {
        method: 'post',
        url: 'http://127.0.0.1:5000/download',
        headers: {
          'Content-Type': 'application/json'
        },
        data: data
      };

      axios(config)
          .then((response) => {
            this.text = JSON.stringify(response.data)
            console.log(JSON.stringify(response.data));
          })
          .catch(function (error) {
            console.log(error);
          });
    },
    find_expand(query_expand) {
      let newQuery = ''
      for (const token of query_expand) {
        newQuery += token + ' '
      }
      this.query = newQuery
      this.find()
    },
    find() {

      const data = JSON.stringify({
        "query": this.query,
        "count": 5,
        "type": this.selected
      });

      const config = {
        method: 'post',
        url: 'http://127.0.0.1:5000/find',
        headers: {
          'Content-Type': 'application/json'
        },
        data: data
      };

      axios(config)
          .then((response) => {
            console.log(JSON.stringify(response.data["data"]));
            this.relevantDocuments = response.data["data"][0]
            this.expand = response.data["data"][1]
            console.log(this.expand)
          })
          .catch(function (error) {
            console.log(error);
          });
    }

  }
}
</script>

<style scoped>

</style>
