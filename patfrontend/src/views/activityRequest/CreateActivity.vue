<template>
    <section class="py-100">
        <div class="container">
            <div class="row">
                <div class="col-lg-4">
                    <AuthSideBar />
                </div>
                <div class="col-md-8">
                    <h2>Electronic Activity Request</h2>
                    <form class="inner-add-comments form-contact-1" id="registration-form"
                        @submit.prevent="createActivityRequest">
                        <div class="row">
                            <div class="col-md-12">


                                <div class="mb-3">
                                    <div class="form-group">
                                        <label for="projectw">Project that your working on<span
                                                style="color: red">*</span></label>
                                        <select class="form-control" v-model="activityRequest" id="projectw"
                                            placeholder="Choose a project">
                                            <option v-for="(proj, pk) in project" :key="pk" :value="proj.pk">
                                                {{ proj.projectname }}</option>
                                        </select>

                                    </div>
                                </div>

                                <div class="mb-3">
                                    <div class="form-group">
                                        <label for="activityRequestDescription">Request Description<span style="color: red">*</span></label>
                                        <textarea name="description" id="activityRequestDescription" class="form-control" v-model="description"></textarea>
                                    </div>
                                </div>

                                <div class="mb-3" v-for="(count,index) in activities" :key="index">
                                    <div class="form-group">
                                        <div class="row">
                                            <div class="col-md-3">
                                                <label :for="`product${index}`">Service or Product</label>
                                                <input type="text" placeholder="Product Name" class="form-control"
                                                   v-model="count.service" :name="`product${index}`" :id="`product${index}`">
                                            </div>
                                            <div class="col-md-3">
                                                <label :for="`amount${index}`">Service or Product price</label>
                                                <input type="number" placeholder="100000" class="form-control"
                                                    step="1000" v-model="count.amount" :name="`amount${index}`" :id="`amount${index}`">
                                            </div>
                                            <div class="col-md-3">
                                                <label :for="`frequency${index}`">Frequency</label>
                                                <input type="number" placeholder="1" class="form-control" step="1" v-model="count.frequency" :name="`frequency${index}`" :id="`frequency${index}`">
                                            </div>
                                            <div class="col-md-3">
                                                <div class="btn-group mt-4" role="group" aria-label="Basic example">
                                                    <button type="button" class="btn btn-secondary"
                                                        @click="addRow()">Add</button>
                                                    <button type="button" class="btn btn-secondary"
                                                        @click="removeRow(index)">Remove</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <button class="btn btn-primary btn-user mt-4 btn-block" @click="createActivityRequest">
                                    Submit Activity Request
                                </button>
                            </div>
                        </div>
                    </form>
                    <!-- <div class="form-group">
                        <label for="filter">Search</label>
                        <input type="text" name="filter" id="filter" placeholder="Enter users name, email, or mct number" v-model="keyword">
                    </div> -->

                </div>
            </div>
        </div>
    </section>
</template>

<script>
import AuthSideBar from '@/components/AuthSideBar.vue';
import axios from 'axios';

export default {
    components: { AuthSideBar },
    data() {
        return {
            project: [],
            activities: [
                {
                    service: '',
                    amount: '',
                    frequency: '',
                }
            ],
            count: 1,
            activityRequest: null,
            description : '',
        }
    },
    mounted() {
        this.getAllDonors()
    },
    methods: {
        getAllDonors() {
            axios.get('http://localhost:8000/api/v1/project/').then(response => {
                this.project = response.data
            }).catch(error => {
                console.log(error);
            })
        },

        addRow() {
            this.activities.push({
                service: '',
                amount: '',
                frequency : ''
            })
        },
        removeRow(index){
            this.activities.splice(index,1)
        },
        createActivityRequest(){
            const data = {
                project:this.activityRequest,
                description:this.description,
                requestedbby:JSON.parse(localStorage.getItem('userid')),
                activities:this.activities,
            }
            console.log(data)
            axios.post("http://localhost:8000/api/v1/earequest/",data)
            .then(data=>{
                console.log(data)
                //clear form here
            })
            // alert(JSON.stringify(data))
        }


    } //End of methods

}
</script>

<style scoped>
::-webkit-input-placeholder {
    /* Edge */
    color: rgba(179, 179, 179, 0.41);
}

:-ms-input-placeholder {
    /* Internet Explorer 10-11 */
    color: rgba(179, 179, 179, 0.41);
}

::placeholder {
    color: rgba(179, 179, 179, 0.41);
}
</style>