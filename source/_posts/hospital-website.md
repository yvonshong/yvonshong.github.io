---
title: Hospital Website based on VUE.js+PHP+MySQL
date: 2016-08-01 19:05:39
categories: project
tags: 
- js
- php
- git
toc: true
---

2016.8.1 在#265个issue  #380次merge request后，阶段性的完成了我们的[橙灵诊所管理系统](https://clinic.baichengyiliao.com/spa.php?action=doctorwork.html)

在入职培训期间，我们实习生组成了一个team，大家分模块完成一个项目，项目的内容是一家医院的在线诊所管理系统，从医生工作站，护士工作站，前台工作站，到预约-登记-分诊-接诊-医生门诊-检查-治疗-药房-收费全流程，还有系统设置，病人库，排班，统计报表等内容的前后端。

<!-- more -->

其中我负责的是系统设置里的诊疗费管理medicalFees.vue的前后端，接诊页面的reception.vue的前端，和其中的报告report.vue的前后端，和实验室检查inspect.vue的前后端。并在其中两个模块的开发过程中作为

项目的技术选型为前端使用vue.js+bootstrap，后端使用PHP+Apache，MySQL数据库。

在开发的过程中，我有一些如下的感悟：

 

## 技术经验的积累

PHP的CodeIgniter框架的使用

前端vue.js的使用

vue的理念是数据驱动，利用数据修改样式和样式的内容。

我们的vue的开发过程，大概是利用假数据，定好数据的格式，手撸出前端，并做好数据绑定，所以在进行数据绑定的时候，数据的格式尤为重要。然后调试后端，发POST请求到数据，处理数据为需要的绑定的格式。

git的客户端SourceTree和GitFlow

gitflow最主要的是区分了master-develop，并在develop上建立feature，master上建hotfix。

![gitflow](http://images.cnblogs.com/cnblogs_com/cnblogsfans/771108/o_git-flow-nvie.png)

## 踩的坑

AJAX的POST请求是异步操作


## 一些软件设计

### MVC架构

写后端PHP时，MVC的理念是将接口和实现分离，controller层接受数据，并对数据利用框架进行安全过滤（而不是让POST贯穿整个controller-model），通过传参的方式调用model层进行操作数据库。

所以在model层里面写如何操作数据的方法，在controller层里面写业务逻辑和如何调用model里的方法。

 

model操作数据库，control调用操作，view展现视图

甚至是MVVM（Model-View-ViewModel）

 

### 模块化

在写前端的过程中，由于我们是分组，对不同的模块进行开发，所以我们对我们自己负责的部分无法很好的设计，比如在诊所管理项目中，我们很多地方需要用到病人信息的展示板patientInfo.vue 结果各个小组都是按自己的方法和格式去实现前端发post和后端读取数据库再返回，不同格式的绑定。

这增大了前端代码的冗余和后期维护的难度。显然应该在模块划分的时候，尽量的解耦合和去冗余。

解耦合的目的，不仅仅是利于开发过程中的模块划分，更方便与小组的人员分工，达到并行的开发。

 

## 软件开发流程

我也是第一次接触到公司里面的开发的过程，期间最主要的还是git的使用，以及merge request和issue。

- 理解产品需求，与产品经理问清楚，业务的逻辑细节，前端操作的细节。
- 整理需求，并与产品沟通是否正确。
- 理清数据库结构，和业务操作表的流程
- 根据需求列出接口，可以写出apiDoc，apiDoc的内容涵盖

```
api {post} url
apiParam各个参数
apiParamExample发送post请求的参数格式
apiSuccess返回的数据格式类型，比如json
apiSuccessExample成功时返回的数据格式
```

- 然后进行前后端的开发
- 后端利用postman进行测试
- 进行前后端连通的测试
- 使用git 合并最新的develop，然后发送merge request to develop
- 等待提issue，然后自己在develop上建立hotfix或者feature，关联到issue号


在公司的软件开发，不同于个人开发的地方主要是协作，在代码层面，是需要利用git解决冲突，拉取最新的小组分支或者develop分支

 

## 团队协作

和在人力的协作方面，这次我出现了很多问题，我的两个模块的两个小组，都有着分别不同程度的delay，我们的模块的复杂程度是一方面（需要操作三层的业务数据表），我的分工也是一个方面。

 

#@ 软件工程的理解

软件工程不同于Computer Science计算机科学的地方，在于它更强调一个工程的概念，所以我们在课堂里学到软件工程导论，软件项目管理与实践，都是当时无关紧要的课，现在更突显价值。

